package com.crashx.api.controllers;

import com.crashx.api.models.Crash;
import com.crashx.api.services.CrashService;
import lombok.RequiredArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/v2/crashes")
@RequiredArgsConstructor
public class CrashController {

    private final CrashService crashService;

    @PostMapping("/report")
    public ResponseEntity<Crash> reportCrash(
            @RequestHeader("X-API-KEY") String apiKey,
            @RequestBody Crash crashData
    ) {
        return ResponseEntity.ok(crashService.reportCrash(apiKey, crashData));
    }
}
