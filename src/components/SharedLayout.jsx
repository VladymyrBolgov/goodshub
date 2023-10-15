import { useSearchParams } from "react-router-dom";
import { Outlet } from 'react-router-dom';
import { Container, Header, Logo, Link } from './SharedLayout.styled';
import { SearchBox } from './SearchBox/SearchBox';

import {GiHamburgerMenu} from 'react-icons/gi'
import { MdOutlineShoppingBasket } from 'react-icons/md';
import { GrFavorite } from 'react-icons/gr';
import { BsChatLeft } from 'react-icons/bs';
import { BsPerson } from 'react-icons/bs';

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
          <Link to="/menu"><GiHamburgerMenu /></Link>
          <Link to="/catalog">Catalog</Link>
          <SearchBox value={productName} onChange={updateQueryString} />
          <nav>
            <Link to="/login"><BsPerson /></Link>
            <Link to="/messages"><BsChatLeft /></Link>
            <Link to="/favorites"><GrFavorite /></Link>
            <Link to="/basket"><MdOutlineShoppingBasket /></Link>
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