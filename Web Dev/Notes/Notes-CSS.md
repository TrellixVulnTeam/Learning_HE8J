# CSS

## Grid

---

## Setting up grid

```css
grid-template-rows: 1fr 1fr
grid-template-cols: 3fr 7fr


child components :
    grid-row: 2/3
    grid-column: 2/3

```

---

## Flexbox

In general, flex: 1 doesn't really space out things evenly,
can consider using grid if we want nicely spaced

---

## Centering a div

```css
width: 50%
margin: auto
```

---

## CSS Reset
```css
*, *::before, *::after {
	padding: 0;
	margin:0;
	box-sizing: border-box;
}
html {
font - size: 62.5
}
```

### IMG locks the aspect ratio
```css
object-fit: contain 

// background-size:cover
	background-position: center
```

### Icons 
set font size to resize
```css
font-size:
```

## Icon button
material-ui
icon-button
```
.swipeButtons .MuiIconButton-root{
 background-color:white;
 box-shadow:0px 10px 53px 0px rgba(0,0,0,0.3)!important;
}
```