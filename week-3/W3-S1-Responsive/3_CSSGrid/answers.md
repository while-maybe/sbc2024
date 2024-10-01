### Answer 1 
"header" takes up the top row with "sidebar", and "main" taking the bottom row.
The "header" row takes only the required amount of height with the remaining vertical space being allocated to the "sidebar" and "main" areas.
The property "grid-template-areas" defines area positioning and without it, the task list (table) is pushed to the bottom right of the screen.

### Answer 2
250px represents the (fixed) width of the sidebar, 1fr represents a fraction of 1/(num total fractions defined) which in our case is 1/1 or the total amount of space possible.
As there are no more fractional elements to share the remaining free space with, it will take all the available space.

### Answer 3
Auto will calculate the minimum required amount of space needed to the header height, 1fr will take all the remaning existing vertical space (please see description above as it works in a similar way).

Swapping the values, would give the body the minimum necessary possible height needed with the dashboard taking all the remaining space.

### Answer 4
grid-template-columns: I would do the following:
```css
@media screen and (max-width: 600px) {
    .dashboard-container {
        display: grid;
        grid-template-columns: 1fr;
        grid-template-rows: auto;
        grid-template-areas:
            "header"
            "sidebar"
            "main";
        height: 100vh;
        gap: 10px;
    }
}
```

### Answer 5
The property "gap" creates space *between* elements in a similar way that flex does.
To create an horizontal only gap I would use `gap: 0 10px;` (the first value represents the horizontal gap size and the second value the vertical gap value).
