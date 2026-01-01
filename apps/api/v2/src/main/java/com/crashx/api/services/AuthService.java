package com.crashx.api.services;

import com.crashx.api.models.User;
import com.crashx.api.repositories.UserRepository;
import com.crashx.api.security.JwtService;
import lombok.RequiredArgsConstructor;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;

@Service
@RequiredArgsConstructor
public class AuthService {

    private final UserRepository userRepository;
    private final PasswordEncoder passwordEncoder;
    private final JwtService jwtService;
    private final AuthenticationManager authenticationManager;
    private final UserDetailsService userDetailsService;

    public String register(String email, String password, String fullName) {
        if (userRepository.findByEmail(email).isPresent()) {
            throw new IllegalArgumentException("Email already in use");
        }

        User user = User.builder()
                .email(email)
                .passwordHash(passwordEncoder.encode(password))
                .fullName(fullName)
                .isActive(true)
                .build();
        
        userRepository.save(user);
        
        UserDetails userDetails = userDetailsService.loadUserByUsername(email);
        return jwtService.generateToken(userDetails);
    }

    public String login(String email, String password) {
        authenticationManager.authenticate(
                new UsernamePasswordAuthenticationToken(email, password)
        );
        UserDetails userDetails = userDetailsService.loadUserByUsername(email);
        return jwtService.generateToken(userDetails);
    }
}
