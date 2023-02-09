import React from "react";
import Container from 'react-bootstrap/Container';


const Footer = () => (
    
            <Container fluid style={{ backgroundColor: '#212529', color: '#fff'}}>
                <Container style={{ display: 'flex', justifyContent: 'center', padding: '10px'}}>
                    <div class="container">
                        <span class="sub">© Все права защищены 2023</span>
                    </div>
                </Container>
            </Container>
)

export default Footer;