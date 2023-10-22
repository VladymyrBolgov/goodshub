import React from "react";
// import { Link } from "react-router-dom";
import { Container } from "./Catalog.styled"
import { Link,} from "react-router-dom";
import { NavLink } from 'react-router-dom';


export const Catalog = () => {

  return (
    <main>
      <Container>
        <ul>
        <li>
            <NavLink to="catalogs" > Computers and laptops</NavLink>
        </li>
        <li>
          <Link to="catalogs">Smartphones and Electronics</Link>
        </li>
        <li>
          <Link >Game consoles and components</Link>
          </li>
          <li>
          <Link >Household appliances</Link>
        </li>
        <li>
          <Link >TV and video equipment</Link>
        </li>
        </ul>
      </Container>
      {/* <Outlet /> */} 
    </main>
  );
};