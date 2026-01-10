class CrashReport {
  final String errorMessage;
  final String stackTrace;
  final String? appVersion;
  final Map<String, dynamic>? deviceInfo;
  final String severity;
  final String occurredAt;

  CrashReport({
    required this.errorMessage,
    required this.stackTrace,
    this.appVersion,
    this.deviceInfo,
    this.severity = 'medium',
    required this.occurredAt,
  });

  Map<String, dynamic> toJson() {
    return {
      'error_message': errorMessage,
      'stack_trace': stackTrace,
      if (appVersion != null) 'app_version': appVersion,
      if (deviceInfo != null) 'device_info': deviceInfo,
      'severity': severity,
      'occurred_at': occurredAt,
    };
  }
}
