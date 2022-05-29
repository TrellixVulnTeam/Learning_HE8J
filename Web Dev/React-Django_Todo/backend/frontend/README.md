## Project notes

Styled components

1. style inheritance

```
    const Div = styled.div`
        padding: 10px;
        color: palevioletred;
    `

    const InheritedDiv = styled(Div)`
        border: 1px solid palevioletred;
    `

```

```
    import styled, { css } from ‘styled-components’;

    const baseInputStyles = css`
    border: 1px solid ${({error})=>( error ? `red` : `grey` )};
    border-radius: 4px;
    outline: none;
    padding: 0.5em;
    `;

    export const DefaultInput = styled.input`
    ${baseInputStyles}
    `;

    export const SecondComponent = styled.button`
    ${baseInputStyles}
        /* make changes as needed*/
    `;
```

2. grid

```
<!-- setting up grid -->
grid-template-rows: 1fr 1fr
grid-template-cols: 3fr 7fr


<!-- positioning items -->
grid-row: 2/3
grid-column: 2/3

```
