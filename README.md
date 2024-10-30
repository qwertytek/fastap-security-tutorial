# Handling Security

[tutorial](https://fastapi.tiangolo.com/tutorial/security/first-steps/#how-it-looks)

## Diferences from the tutorial

The tutorial focused on explaining each piece of code, while visualizing everything on the same file.
Although I like this approach, separating each piece of logic into it's on file massively improved my understanding of the Security implementation. As there alot of concepts that are needed to be understood to be able to add your own authentication flows. On a single file it's easy to loose track of the interactions.

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

### Hashing, enconding and decoding

- Hashing
Hashing is a process that transforms data of any size into a fixed-size value, usually a string of letters and numbers.
  - One-way process, meaning it’s extremely difficult to reverse. You cannot "decode" a hash to get the original data back.
  - Primarily used for security purposes (e.g., storing passwords securely) and data integrity (e.g., ensuring files haven’t been altered).
  - specifically designed to secure sensitive data through one-way encryption and to detect tampering.
  - The same input always produces the same hash, which is useful for verification.

- Encoding
Transforming data into a different format to ensure it’s readable or compatible with various systems.
  - designed to be reversible
  - make data safe for transmission or storage, handling special characters, or ensuring compatibility.
  - It is not meant for security and offers no protection against unauthorized access.

- Decoding
The reverse of encoding. If something was encoded, you can decode it to get back the original data.
  - Used in data transmission and storage to handle non-standard characters or compress data.
