library crashx;

import 'dart:async';
import 'src/crashx_impl.dart';

export 'src/models/crash_report.dart';

/// The entry point for CrashX analytics.
class CrashX {
  /// Initializes the CrashX plugin.
  ///
  /// [apiKey] is your project's API Key.
  static Future<void> init({required String apiKey}) async {
    await CrashXImpl().init(apiKey: apiKey);
  }

  /// Manually records an error.
  ///
  /// [exception] is the error object.
  /// [stack] is the stack trace.
  static void recordError(dynamic exception, StackTrace? stack) {
    CrashXImpl().recordError(exception, stack);
  }
}
