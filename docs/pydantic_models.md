# Pydantic model help and cheat sheet

## Difference between BaseModel and GenericModel

Pydantic's `BaseModel` and `GenericModel` serve different purposes, and understanding their use cases is crucial for
structuring your data models effectively.

### Pydantic's `BaseModel`

- **Primary Use**: `BaseModel` is the core feature of Pydantic used for defining data structures. It allows you to
  create classes that include type annotations, validation, serialization, and deserialization. Essentially, it's used
  to create concrete models with predefined fields.

- **Features**:
    - **Type Annotations**: You can use Python's type annotations to specify the type of each field.
    - **Validation**: Automatic validation of input data according to the field types.
    - **Serialization/Deserialization**: Easily convert models to and from JSON, dictionaries, etc.
    - **Customization**: Customize validation, parsing, and serialization behavior.

- **When to Use**: Use `BaseModel` when you need to define a specific data structure with known fields. It's ideal for
  most use cases where your data schema is predetermined and does not need to be generic.

### Pydantic's `GenericModel`

- **Primary Use**: `GenericModel` is an extension of `BaseModel` that supports the creation of generic models. This
  means you can define models where some fields are left to be specified later, using Python's typing generics.

- **Features**:
    - **Generics Support**: Allows for type parameters, making the model reusable for different types. This is
      particularly useful for creating base models that can be adapted for various data types.
    - **Dynamic Data Structures**: Ideal for scenarios where the exact type of some fields is not known in advance and
      depends on the usage context.

- **When to Use**: Use `GenericModel` when you need a model that is flexible with regard to the type of some of its
  fields. It's particularly useful for building base models or abstract models in frameworks, libraries, or applications
  where you want to reuse the same structure for different data types.

### Example Comparison

To illustrate, consider an API response model:

- **Using `BaseModel`**: If every response has a fixed structure, say `data`, `error`, and `timestamp` fields, you would
  use `BaseModel` to define this concrete structure.

- **Using `GenericModel`**: If the `data` field in the response can be of multiple types (like a single object, a list
  of objects, etc.), you might use `GenericModel` to create a generic response model where the type of `data` can be
  specified when the model is used.

In summary, choose `BaseModel` for concrete, known data structures, and `GenericModel` for flexible, reusable models
where some fields' types are determined at runtime.