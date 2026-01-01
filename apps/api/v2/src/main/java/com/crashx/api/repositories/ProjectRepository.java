package com.crashx.api.repositories;

import com.crashx.api.models.Project;
import org.springframework.data.jpa.repository.JpaRepository;
import java.util.List;
import java.util.Optional;
import java.util.UUID;

public interface ProjectRepository extends JpaRepository<Project, UUID> {
    Optional<Project> findByApiKey(String apiKey);
    List<Project> findByUserId(UUID userId);
}
