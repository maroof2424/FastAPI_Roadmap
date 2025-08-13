## **📅 Week 2: CRUD + Pydantic + Routers**

---

### **🔹 Day 1 – Project Setup + Basic Router**

**Goals:**

* Create `APIRouter`
* Register router in `main.py`
* Create `/posts` GET endpoint (dummy data)

**Tasks:**

1. Create `app/routers/posts.py`
2. Add dummy `GET /posts` returning a list of posts
3. Register it in `main.py`

---

### **🔹 Day 2 – Schemas (Pydantic)**

**Goals:**

* Create `PostCreate` & `PostOut` models in `schemas.py`
* Learn to validate request body using Pydantic

**Tasks:**

1. `PostCreate` → for incoming POST requests
2. `PostOut` → for outgoing responses (hide `internal_id`)
3. Implement `POST /posts` using schema

---

### **🔹 Day 3 – CRUD Logic (In-Memory)**

**Goals:**

* Create `crud.py` to separate data logic
* Implement `create_post` & `get_posts`

**Tasks:**

1. Store posts in a Python list
2. Auto-generate IDs
3. Return created post

---

### **🔹 Day 4 – GET by ID + PUT**

**Goals:**

* Implement `GET /posts/{id}`
* Implement `PUT /posts/{id}`

**Tasks:**

1. Validate `id` exists
2. Update post details using schema
3. Return updated post

---

### **🔹 Day 5 – DELETE**

**Goals:**

* Implement `DELETE /posts/{id}`
* Return success message if deleted

**Tasks:**

1. Check if post exists
2. Remove from list
3. Return status message

---

### **🔹 Day 6 – Query & Path Parameters**

**Goals:**

* Implement search using query parameters
* Example: `/posts/search?keyword=python`

**Tasks:**

1. Add keyword filtering
2. Return matching posts only

---

### **🔹 Day 7 – Response Models & Final Cleanup**

**Goals:**

* Ensure all routes use `response_model`
* Remove sensitive/internal fields from output

**Tasks:**

1. Add `response_model` to all endpoints
2. Clean `crud.py` functions
3. Test API in Swagger docs

---

If you want, I can **give you the exact code for each day** so you can copy into
`routers/`, `schemas.py`, `crud.py`, and `main.py` while learning how each part works.
That way, by the end of Week 2, your Blog API will be fully functional.


