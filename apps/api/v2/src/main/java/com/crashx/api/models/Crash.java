package com.crashx.api.models;

import jakarta.persistence.*;
import lombok.*;
import org.hibernate.annotations.GenericGenerator;
import java.util.UUID;
import java.time.LocalDateTime;

@Entity
@Table(name = "crashes")
@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class Crash {
    @Id
    @GeneratedValue(generator = "UUID")
    @GenericGenerator(name = "UUID", strategy = "org.hibernate.id.UUIDGenerator")
    @Column(updatable = false, nullable = false)
    private UUID id;

    @Column(nullable = false)
    private String errorMessage;

    @Column(columnDefinition = "TEXT", nullable = false)
    private String stackTrace;

    private String appVersion;
    
    @Column(columnDefinition = "TEXT")
    private String deviceInfo; // Storing JSON as string for simplicity

    @Enumerated(EnumType.STRING)
    private Severity severity;
    
    @Enumerated(EnumType.STRING)
    private Status status;

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "project_id", nullable = false)
    private Project project;

    @Builder.Default
    private LocalDateTime occurredAt = LocalDateTime.now();

    public enum Severity {
        LOW, MEDIUM, HIGH, CRITICAL
    }

    public enum Status {
        OPEN, RESOLVED, IGNORED
    }
}
