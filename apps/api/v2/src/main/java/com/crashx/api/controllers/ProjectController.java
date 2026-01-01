package com.crashx.api.controllers;

import com.crashx.api.models.Project;
import com.crashx.api.services.ProjectService;
import lombok.Data;
import lombok.RequiredArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.security.core.annotation.AuthenticationPrincipal;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/v2/projects")
@RequiredArgsConstructor
public class ProjectController {

    private final ProjectService projectService;

    @PostMapping
    public ResponseEntity<Project> createProject(
            @RequestBody CreateProjectRequest request,
            @AuthenticationPrincipal UserDetails userDetails
    ) {
        return ResponseEntity.ok(projectService.createProject(
                request.getName(),
                request.getDiscordWebhookUrl(),
                userDetails.getUsername()
        ));
    }

    @GetMapping
    public ResponseEntity<List<Project>> getMyProjects(@AuthenticationPrincipal UserDetails userDetails) {
        return ResponseEntity.ok(projectService.getUserProjects(userDetails.getUsername()));
    }

    @Data
    public static class CreateProjectRequest {
        private String name;
        private String discordWebhookUrl;
    }
}
