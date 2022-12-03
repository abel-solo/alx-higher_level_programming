# JavaScript - Objects, Scopes and Closures
---
### An object is a collection of related data and/or functionality. These usually consist of several variables and functions (which are called properties and methods when they are inside objects).

---

### As with many things in JavaScript, creating an object often begins with defining and initializing a variable. Try entering the following line below the JavaScript code that's already in your file, then saving and refreshing:

``` javascript
const person = {};
```
### Now open your browser's JavaScript console, enter person into it, and press Enter/Return. You should get a result similar to one of the below lines

``` javascript
[object Object]
Object { }
{ }
```

### Congratulations, you've just created your first object. Job done! But this is an empty object, so we can't really do much with it. Let's update the JavaScript object in our file to look like this:

``` javascript
const person = {
  name: ["Bob", "Smith"],
  age: 32,
  bio: function () {
    console.log(`${this.name[0]} ${this.name[1]} is ${this.age} years old.`);
  },
  introduceSelf: function () {
    console.log(`Hi! I'm ${this.name[0]}.`);
  },
};
```


