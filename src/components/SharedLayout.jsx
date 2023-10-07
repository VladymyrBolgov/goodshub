import { useSearchParams } from "react-router-dom";
import { Outlet } from 'react-router-dom';
import { Container, Header, Logo, Link } from './SharedLayout.styled';
import { SearchBox } from './SearchBox/SearchBox';

export const SharedLayout = () => {
  const [searchParams, setSearchParams] = useSearchParams();
  const productName = searchParams.get("name") ?? "";

  const updateQueryString = (name) => {
    const nextParams = name !== "" ? { name } : {};
    setSearchParams(nextParams);
  };
    return (
      <Container>
        <Header>
          <Logo>
            <Link to="/" end>GoodsHub</Link>
          </Logo>
          <Link to="/catalog">Catalog</Link>
          <SearchBox value={productName} onChange={updateQueryString} />
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

// export const SharedLayout = () => {
//     return (
//       <>
//       <Header />
//       <Outlet />
//     </>
//     );
//   };