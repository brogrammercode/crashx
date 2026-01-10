import 'dart:convert';
import 'package:http/http.dart' as http;
import 'models/crash_report.dart';

class ApiClient {
  final String apiKey;

  ApiClient({required this.apiKey});

  Future<void> sendCrashReport(CrashReport report) async {
    final apiUrl = 'https://crashx-fz8b.vercel.app/api/v1';
    final uri = Uri.parse('$apiUrl/crashes/report');
    try {
      final response = await http.post(
        uri,
        headers: {'Content-Type': 'application/json', 'x-api-key': apiKey},
        body: jsonEncode(report.toJson()),
      );

      if (response.statusCode != 200 && response.statusCode != 201) {
        print(
          'CrashX: Failed to send report. Status code: ${response.statusCode}',
        );
        print('CrashX: Response: ${response.body}');
      }
    } catch (e) {
      print('CrashX: Error sending report: $e');
    }
  }
}
