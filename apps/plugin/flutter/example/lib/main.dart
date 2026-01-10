import 'package:flutter/material.dart';
import 'package:crashx/crashx.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();

  // Replace with your actual API Key
  await CrashX.init(
    apiKey: "YOUR_API_KEY_HERE",
  );

  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: const Text('CrashX Example'),
        ),
        body: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              const Text('Press the buttons to test CrashX'),
              const SizedBox(height: 20),
              ElevatedButton(
                onPressed: () {
                  // Test manual error reporting
                  try {
                    throw Exception(
                        "This is a manual test exception from CrashX Example");
                  } catch (e, stack) {
                    CrashX.recordError(e, stack);
                    ScaffoldMessenger.of(context).showSnackBar(
                      const SnackBar(content: Text('Manual error recorded')),
                    );
                  }
                },
                child: const Text('Record Manual Error'),
              ),
              const SizedBox(height: 20),
              ElevatedButton(
                onPressed: () {
                  // Test automatic uncaught error reporting
                  throw Exception(
                      "This is an uncaught test exception from CrashX Example");
                },
                child: const Text('Throw Uncaught Error'),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
