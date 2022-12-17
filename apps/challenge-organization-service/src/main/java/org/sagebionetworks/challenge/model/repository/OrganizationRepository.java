package org.sagebionetworks.challenge.model.repository;

import java.util.Optional;
import org.sagebionetworks.challenge.model.entity.OrganizationEntity;
import org.springframework.data.jpa.repository.JpaRepository;

public interface OrganizationRepository extends JpaRepository<OrganizationEntity, Long> {

  Optional<OrganizationEntity> findByLogin(String login);
}
