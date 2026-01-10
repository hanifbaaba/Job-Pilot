## JobPilot

- JobPilot is a job application platform that allows candidates to apply for jobs, companies to Post job opportunities. It provides a clean API backend built with Django & DRF, optimized for performance, scalability, and production deployment.

## Table of Content

- Features
- Installation
- System Design
- Usage
- Endpoints
- Email notifications
- Tech Stack
- Contributions
- License
- Author

## Features

- Job application for job seekers.
- Job creation for employers.
- Search with filters based on categories(title, keyword,location,salary etc)
- Pagination
- Email Notification
- Resume upload
- Secure and scalable architecture

## Installation

1. Clone the repository

- git clone https://github.com/hanifbaaba/JobPilot
- Enter the directory:
- cd backend
- Install required dependencies:
- pip install -r requirements.txt
- Run the project:
- python manage.py runserver

## System Design

JobPilot System Design

Architecture

- Monolith Backend Application
- Client → Server → PostgreSQL DB
- File Storage via Amazon S3
- HTTPS for secure communication

Features

- Job creation
- Job application
- Resume upload
- Email Notifications
- Pagination
- Searching and filtering
- Deployment

Data Model Definitions
CreateJob

- job_title
- description
- salary
- company_name
- location
- category
- experience
- created_at
- updated_at

ApplyJob

- job(FK)
- name
- email
- reason_for_applying
- country_of_residence
- resume_upload
- portfolio_link
- preferred_salary

Engineering Requirements

- Extensibility : Future feature (frontend integration, live interviews etc)
- Testing : Testing live endpoints with Swagger
- API Stability : Clear routing and consistent response structure

Non-Functional Requirements

- Performance : Redis caching for frequently searched queries
- Reliability : 99% uptime with target with monolith architecture and Backup DB
- Security : HTTPS encryption , CSRF protection
- Resilience : Additional nodes, Backup DB
- Scalability : Vertical scaling and load balancing(Round robin and geo-based) after 10,000 users
- Logging and metrics : Python logging
- CDN : Static assets
- File storage : Amazon S3 for resumes

Low-Level Design

- Job seekers → search, filter, view, and apply
- Employers → create and manage job listings

Memory Optimization:

- Pagination
- Lazy loading
- Caching: Redis for search & repeated queries\

API Design

- Proper HTTP methods (GET, POST, PUT, DELETE)
- Each endpoint has a single clear responsibility

Error Handling:

- 400 → Bad Request
- 401 → Unauthorized
- 404 → Not Found
- 500 → Server Error

Pagination: 10 jobs per page

- Defensive routing to avoid improper requests

Database & Storage

- Primary DB: PostgreSQL
- File Storage: Amazon S3
- Backup DB: MongoDB node for resilience

## Usage

Job Seeker

- Create an account
- Log in
- Search for jobs
- Apply to a job
- Receive recruiter feedback

Employer

- Post new job listings
- Manage posted jobs
- Contact candidates via email

## API Endpoints

- Creating a new job.
  GET/create-job this displays list of available jobs.
  [
  {
  "id": 1,
  "job_title": "Frontend developer",
  "description": "We are looking for a highly talented frontend developer experienced in React and typescript. Must be familiar with git and aws deployment.",
  "salary": "96000.00",
  "company_name": "daea",
  "location": "Remote",
  "category": "Frontend development"
  },
  {
  "id": 2,
  "job_title": "Backend developer",
  "description": "We are looking for a highly talented Backend developer experienced in Django and PostgreSQL. Must be familiar with git and aws deployment.",
  "salary": "95000.00",
  "company_name": "daea",
  "location": "Remote",
  "category": "Backend development"
  },
  {
  "id": 3,
  "job_title": "Data Scientist",
  "description": "We are hiring a data scientist to join our team . Qualifications must be able to use numpy, matplotlib and 10 years of experience.",
  "salary": "960000.00",
  "company_name": "daea",
  "location": "Remote",
  "category": "Data Science"
  }
  ]
  GET /create-job/<id>/ gets a single job
  {
  "id": 2,
  "job_title": "Backend developer",
  "description": "We are looking for a highly talented Backend developer experienced in Django and PostgreSQL. Must be familiar with git and aws deployment.",
  "salary": "95000.00",
  "company_name": "daea",
  "location": "Remote",
  "category": "Backend development"
  },
  POST/create-job this creates a new job application.
  PUT/create-job<id>/ this updates a job application.
  DELETE/create-job<id>/ this deletes a job application.

- Applying for a job
  GET /apply-job/<id> Returns all job applications.
  POST /apply-job/<id> Submit a new application.
  {
  "job": 2,
  "name": "John Doe",
  "reason_for_applying": "I have strong experience…",
  "country_of_residence": "USA",
  "portfolio_link": "https://portfolio.dev"
  }
  PUT /apply-job/<id> Updates job application
  DELETE /apply-job/<id> Deletes job application

- Searching for jobs based on filter
  this endpoint search for jobs based on keywords in the url
  Example

  - /create-job/?search=developer
  - /create-job/?search=data
  - /create-job/?search=manager
  - /create-job/?search=engineer

- Salary range based filtering

  - /create-job/?min_salary=200000 User will be able to search the minimum salary posted
  - /create-job/?max_salary=600000 User will be able to search the maximum salary posted
  - /create-job/?min_salary=200000&max_salary=600000 User will be able to search for both minimum amount and maximum amount

- Pagination
  Example
  GET /apply-job/?page = 4. This will route to page 4 of jobs application page.

Response:

HTTP 200 OK
{
"count": 80,
"next": "/apply-job/?page=5",
"previous": "/apply-job/?page=3",
"results": [
Job applications results
]
}

## Email Notification

When a user applies for a job, they will get instant email feedback from the recruiter. It utilizes django's send_mail() concept.

## Tech Stack

- Language : Python
- Framework : Django, Django Rest Framework
- Database : PostgreSQL/MongoDB
- Deployment : Render/Railway

## Contributing

- Fork the repo
- Create a new branch ("git checkout -b feature-branch)
- Commit new changes ("git commit -m "Added a new feature")
- Push to your branch ("git push origin feature-branch")
- Open a pull request

## License

- This project is under the MIT license.

## Author

- Hanif Baaba
- Github : (https://github.com/hanifbaaba)
