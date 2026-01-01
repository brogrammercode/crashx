package com.crashx.api.services;

import com.crashx.api.models.Crash;
import org.springframework.scheduling.annotation.Async;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

@Service
public class DiscordService {

    private final RestTemplate restTemplate = new RestTemplate();

    @Async
    public void sendCrashAlert(String webhookUrl, Crash crash, String projectName) {
        if (webhookUrl == null || webhookUrl.isEmpty()) return;

        Map<String, Object> payload = new HashMap<>();
        Map<String, Object> embed = new HashMap<>();

        embed.put("title", "🚨 Crash in " + projectName);
        embed.put("description", "**Error**: " + crash.getErrorMessage());
        embed.put("color", getColorForSeverity(crash.getSeverity()));
        
        // Fields
        List<Map<String, Object>> fields = List.of(
            Map.of("name", "Severity", "value", crash.getSeverity().toString(), "inline", true),
            Map.of("name", "App Version", "value", crash.getAppVersion() != null ? crash.getAppVersion() : "Unknown", "inline", true),
            Map.of("name", "Device", "value", crash.getDeviceInfo() != null ? crash.getDeviceInfo() : "Unknown", "inline", false),
            Map.of("name", "Stack Trace", "value", "```" + truncate(crash.getStackTrace(), 1000) + "```")
        );
        
        embed.put("fields", fields);
        payload.put("embeds", List.of(embed));

        try {
            restTemplate.postForEntity(webhookUrl, payload, String.class);
        } catch (Exception e) {
            System.err.println("Failed to send Discord webhook: " + e.getMessage());
        }
    }

    private int getColorForSeverity(Crash.Severity severity) {
        return switch (severity) {
            case LOW -> 0x3498db;
            case MEDIUM -> 0xf1c40f;
            case HIGH -> 0xe67e22;
            case CRITICAL -> 0xe74c3c;
        };
    }
    
    private String truncate(String str, int len) {
        if (str.length() > len) {
            return str.substring(0, len) + "...";
        }
        return str;
    }
}
