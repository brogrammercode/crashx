package com.crashx.api.repositories;

import com.crashx.api.models.Crash;
import org.springframework.data.jpa.repository.JpaRepository;
import java.util.List;
import java.util.UUID;

public interface CrashRepository extends JpaRepository<Crash, UUID> {
    List<Crash> findByProjectId(UUID projectId);
}
