# Handling Security

[tutorial](https://fastapi.tiangolo.com/tutorial/security/first-steps/#how-it-looks)

## Diferences from the tutorial

The tutorial focused on explaining each piece of code, while visualizing everything on the same file.
Although I like this approach, separating each piece of logic into it's on file massively improved my understanding of the Security implementation. As there alot of concepts that are needed to be understood to be able to add your own authentication flows.

## Key Concepts

### Dependency Injection

If you are a begginer using fastapi, this is an important concept you need to master.
Depedency injection is a technique used in [OOP](https://en.wikipedia.org/wiki/Object-oriented_programming).
In this context, a dependency is any component or function that requires another object or service from the app to execute its role properly.

It's widely used and it will simplify the logic of your code if used properly.
In the case of this tutorial, alot of it is about creating the token, OAUTH and database connection.
The reason why putting it in dependency is that writting the same logic for every place that it needs to be used goes against the [DRY principle](https://en.wikipedia.org/wiki/Don%27t_repeat_yoursel).

Still confused about dependency injection, here are some unusual ways to describe it:

Dependency injection is like:
    - callable local variables. (callable in the sense that you request your variables where you need them)
    - A function that returns and object

Key benefits of using dependency injection

- Automatic setup: FastAPI calls your dependency function only when needed, so you don’t have to manually initialize or pass objects everywhere.
- On-demand delivery: Your routes and functions stay clean, focusing only on their main job, while dependencies arrive "on demand."
- Reusability: Any function that needs a dependency can simply request it, making code more modular and consistent

### Pydantic Models

Pydantic is data validation library for Python. It comes installed with fastapi.
Use this define your models.

### database

For this tutorial I skipped this step, as only the data is needed. It will be in a separate file with mock data.
