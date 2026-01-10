import 'dart:async';
import 'dart:io';
import 'package:flutter/foundation.dart';
import 'package:device_info_plus/device_info_plus.dart';
import 'package:package_info_plus/package_info_plus.dart';
import 'api_client.dart';
import 'models/crash_report.dart';

class CrashXImpl {
  static final CrashXImpl _instance = CrashXImpl._internal();
  factory CrashXImpl() => _instance;
  CrashXImpl._internal();

  ApiClient? _apiClient;
  Map<String, dynamic>? _deviceInfo;
  String? _appVersion;
  bool _initialized = false;

  Future<void> init({required String apiKey}) async {
    if (_initialized) return;

    _apiClient = ApiClient(apiKey: apiKey);
    await _loadMetadata();

    // Set up global error handling
    FlutterError.onError = _handleFlutterError;
    PlatformDispatcher.instance.onError = _handlePlatformError;

    _initialized = true;
    print('CrashX: Initialized');
  }

  Future<void> _loadMetadata() async {
    try {
      final packageInfo = await PackageInfo.fromPlatform();
      _appVersion = packageInfo.version;

      final deviceInfoPlugin = DeviceInfoPlugin();
      if (kIsWeb) {
        final webInfo = await deviceInfoPlugin.webBrowserInfo;
        _deviceInfo = {
          'os': 'web',
          'browser': webInfo.browserName.name,
          'version': webInfo.appVersion,
        };
      } else if (Platform.isAndroid) {
        final androidInfo = await deviceInfoPlugin.androidInfo;
        _deviceInfo = {
          'os': 'android',
          'version': androidInfo.version.release,
          'manufacturer': androidInfo.manufacturer,
          'model': androidInfo.model,
        };
      } else if (Platform.isIOS) {
        final iosInfo = await deviceInfoPlugin.iosInfo;
        _deviceInfo = {
          'os': 'ios',
          'version': iosInfo.systemVersion,
          'model': iosInfo.model,
          'name': iosInfo.name,
        };
      }
    } catch (e) {
      print('CrashX: Failed to load metadata: $e');
    }
  }

  void _handleFlutterError(FlutterErrorDetails details) {
    recordError(details.exception, details.stack, fatal: true);
    // Call original handler if needed, or default dumping
    FlutterError.presentError(details);
  }

  bool _handlePlatformError(Object error, StackTrace stack) {
    recordError(error, stack, fatal: true);
    return true;
  }

  void recordError(dynamic exception, StackTrace? stack, {bool fatal = false}) {
    if (!_initialized || _apiClient == null) {
      print('CrashX: Not initialized. Cannot record error.');
      return;
    }

    final report = CrashReport(
      errorMessage: exception.toString(),
      stackTrace: stack?.toString() ?? StackTrace.current.toString(),
      appVersion: _appVersion,
      deviceInfo: _deviceInfo,
      occurredAt: DateTime.now().toUtc().toIso8601String(),
      severity: fatal ? 'critical' : 'medium', // Simple mapping
    );

    _apiClient!.sendCrashReport(report);
  }
}
