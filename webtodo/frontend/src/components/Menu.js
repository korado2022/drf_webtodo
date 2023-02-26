import Container from 'react-bootstrap/Container';
import React from "react";
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import Button from 'react-bootstrap/Button';




const NaviBar = (props) => {
    const is_in = [props.is_in][0];
    return (
        <>
        <Navbar collapseOnSelect expand="lg" bg="dark" variant="dark">
            <Container>
                <Navbar.Brand>Web ToDo</Navbar.Brand>
                <Navbar.Toggle aria-controls="responsive-navbar-nav" />
                <Navbar.Collapse id="responsive-navbar-nav">
                    <Nav className="me-2">
                        <Nav.Link href='/users'>Все пользователи</Nav.Link>
                        <Nav.Link href='/projects'>Проекты</Nav.Link>
                        <Nav.Link href='/todos'>To Do</Nav.Link>
                    </Nav>
                </Navbar.Collapse>
                <Navbar.Collapse className="justify-content-end">
                    <Nav>
                        <Button variant="primary" className="me-2 d-flex is_in" href='/login' disabled={is_in}>Log In</Button>
                        <Button variant="primary" className="me-2 d-flex" disabled={!is_in}
                            onClick={() => props.logout()} href='/login'>Sing Out</Button>
                    </Nav>
                </Navbar.Collapse>
            </Container>
        </Navbar>
        </>
    );
    console.log(this.props.token)
}

export default NaviBar;