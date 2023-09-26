import { Routes, Route } from "react-router-dom";

import { HomePage } from "../pages/HomePage/HomePage";
import {RegisterPage} from "../pages/RegisterPage/RegisterPage"
import { LoginPage } from "../pages/LoginPage/LoginPage";
import { NotFoundPage } from "../pages/NotFoundPage/NotFoundPage";
import { Catalog } from "../pages/Catalog/Catalog";
import { Favorites } from "../pages/Favorites/Favorites";
import { Basket } from "../pages/Basket.jsx/Basket";

import { Container, Header, Logo, Link } from "./App.styled";

export const App = () => {
  return (
    <Container>
       <Header>
        <Logo>
          <span role="img" aria-label="computer icon">
            💻
          </span>{" "}
          <Link to="/" end>GoodsHub</Link>
        </Logo>
        <nav>
          <Link to="/catalog">Catalog</Link>
          <Link to="/" end>Home</Link>
          <Link to="/login">Login</Link>
          <Link to="/favorites">Favorites</Link>
          <Link to="/basket">Basket</Link>
        </nav>
      </Header>

      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/catalog" element={<Catalog />} />
        <Route path="/register" element={<RegisterPage />} />
        <Route path="/login" element={<LoginPage />} />
        <Route path="/favorites" element={<Favorites />} />
        <Route path="/basket" element={<Basket />} />
        <Route path="*" element={<NotFoundPage/>} /> 
      </Routes>
    </Container>
  );
};
