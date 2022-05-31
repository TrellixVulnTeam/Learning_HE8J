# Style components

---

## Targetting components

```js
const hello  = styled.div`

    &:hover ${anothercomponent's name} {
        whatever styles
    }`

```

---

## Inheritance

```js
const Div = styled.div`
  padding: 10px;
  color: palevioletred;
`

const InheritedDiv = styled(Div)`
  border: 1px solid palevioletred;
`
```

---

## Use CSS directly

```js
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
