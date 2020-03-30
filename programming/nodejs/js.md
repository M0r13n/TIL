# Javascript

### Usefull

`dir` but for JS: `Object.keys(object)`


### Iterating over arrays:
Only iterate:

```js
const array = ["one", "two", "three"]
array.forEach(function (item, index) {
  console.log(item, index);
});
```

with filter:
```js
array.filter(item => item.condition < 10)
     .forEach(item => console.log(item));
```

Create a new array from existing. DO not use for each. USE map

```js
const numbers = [1,2,3,4,5];
const doubled = numbers.map(n => n * 2);
```


Reduce:
```js
const numbers = [1,2,3,4,5];
const sum = numbers.reduce((total, n) => total + n, 0);
```


For ... of (for those Python lovers)
```js
let colors = ['red', 'green', 'blue'];
for (const color of colors){
    console.log(color);
}
```
