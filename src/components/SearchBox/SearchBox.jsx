import { Wrapper, Input, Icon, Button } from "./SearchBox.styled";

export const SearchBox = ({ value, onChange }) => {
  return (
      <Wrapper>
      <Icon />
      <Input
        type="text"
        value={value}
              onChange={(e) => onChange(e.target.value)}    
          />
        <Button>Search</Button>
    </Wrapper>
  );
};