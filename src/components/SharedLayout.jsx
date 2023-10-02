import { Outlet } from 'react-router-dom';
import { Container, Header, Logo, Link } from './SharedLayout.styled';

export const SharedLayout = () => {
  return (
      <Container>
        <Header>
          <Logo>
            <span role="img" aria-label="computer icon">
              💻
            </span>{" "}
              <Link to="/" end>GoodsHub</Link>
          </Logo>
              <Link to="/catalog">Catalog</Link>
        <nav>
          <Link to="/login">Login</Link>
          <Link to="/messages">Messages</Link>
          <Link to="/favorites">Favorites</Link>
          <Link to="/basket">Basket</Link>
        </nav>
      </Header>
        <Outlet />
      </Container>
    );
  };