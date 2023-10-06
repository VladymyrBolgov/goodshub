import { Wrapper, Input, Icon, Button } from "./SearchBox.styled";
import { useSearchParams } from "react-router-dom";

export const SearchBox = () => {
    
    const [searchParams, setSearchParams] = useSearchParams();
    const productId = searchParams.get('productId');
   
  return (
      <Wrapper>
      <Icon />
      <Input
        type="text"
        value={productId}
        onChange= {(e) => setSearchParams({productId: e.target.value})}    
          />
        <Button onClick={() => setSearchParams({productId: 'productId'})}>Search</Button>
    </Wrapper>
  );
};