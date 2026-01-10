# CrashX

A Flutter plugin for CrashX analytics. specific for flutter apps.

## Features

*   **Automatic Error Catching**: Hooks into `FlutterError.onError` and `PlatformDispatcher.instance.onError` to capture uncaught exceptions.
*   **Metadata Collection**: Automatically collects device info (OS, Model, Version) and App Version.
*   **Manual Reporting**: Manually report errors using `CrashX.recordError`.
*   **Offline Support**: (Coming Soon)

## Getting Started

1.  Add `crashx` to your `pubspec.yaml` dependencies.
2.  Initialize the plugin in your `main.dart`.

```dart
import 'package:flutter/material.dart';
import 'package:crashx/crashx.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  
  // Initialize CrashX with your API Key
  await CrashX.init(
    apiKey: "YOUR_PROJECT_API_KEY",
  );

  runApp(const MyApp());
}
```

## Usage

### Automatic capturing

Once initialized, CrashX automatically captures uncaught errors in your Flutter app.

### Manual capturing

You can also manually report errors:

```dart
try {
  // Some dangerous code
} catch (e, stack) {
  CrashX.recordError(e, stack);
}
```
