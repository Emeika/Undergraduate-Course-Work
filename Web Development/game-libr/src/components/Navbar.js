// src/components/Navbar.js
import React from 'react';
import { Navbar, Nav, Container } from 'react-bootstrap';
import '../styles/Navbar.css';

const Navigation = () => {
    return (
        <Navbar className="navbar-custom" expand="lg">
        <Container fluid className='py-0'>
            <Navbar.Brand href="#" className="d-flex align-items-center">
                <img
                    src="/assets/logo-nav.png"  // Replace with the path to your second image
                    alt="icon"
                        height="50"
                        width = "60"
                    className="d-inline-block align-top"
                />
            {' '}
            <img
                src="/assets/logo-text.png"  // Replace with the path to your logo
                alt="Logo"
                height="30"
                className="d-inline-block"
                        
            />
            </Navbar.Brand>

            {/* Toggle button for mobile view */}
            <Navbar.Toggle aria-controls="basic-navbar-nav" />

            {/* Menu options on the right */}
            <Navbar.Collapse id="basic-navbar-nav" className="justify-content-end">
            <Nav>
                <Nav.Link href="#discover">Discover</Nav.Link>
                <Nav.Link href="#login-signup">Login/Signup</Nav.Link>
            </Nav>
            </Navbar.Collapse>
        </Container>
        </Navbar>
    );
};

export default Navigation;
