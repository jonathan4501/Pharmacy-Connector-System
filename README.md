# Pharmacy Connector System

A robust Django-based backend system for managing pharmacy operations, inventory, sales, orders, and webhook integrations. The system exposes a secure RESTful API for integration with external pharmacy systems, supports real-time features with Django Channels, and background tasks with Celery.

## Features

- **Pharmacy Management**: Register and manage multiple pharmacies, each with unique API keys and webhook URLs.
- **Inventory Management**: Track inventory items, quantities, and prices per pharmacy.
- **Sales Tracking**: Record sales transactions, quantities, and total prices.
- **Order Management**: Manage orders, statuses, and order items.
- **Webhook Events**: Receive and process webhook events from external systems.
- **API Key Authentication**: Secure API access for each pharmacy using unique API keys.
- **Admin Dashboard**: Full CRUD via Django admin for all models.
- **API Documentation**: Interactive Swagger and Redoc documentation.
- **Background Tasks**: Celery integration for asynchronous/background processing.
- **Real-time Support**: Django Channels and Redis for real-time features.

## Technology Stack

- Python 3.x
- Django 5.x
- Django REST Framework
- Django Channels (WebSockets)
- Celery (with Redis broker)
- PostgreSQL (default, configurable)
- drf-yasg (API docs)
- Jazzmin (admin UI)

## Database Models

### Pharmacy
- `name`: Name of the pharmacy
- `api_key`: Unique API key for authentication
- `webhook_url`: Optional URL for receiving webhooks
- `is_active`: Whether the pharmacy is active
- `created_at`, `updated_at`: Timestamps

### InventoryItem
- `pharmacy`: ForeignKey to Pharmacy
- `sku`, `name`, `quantity`, `price`: Item details
- `extra_data`: JSON field for extensibility
- `updated_at`: Timestamp

### Sale
- `pharmacy`: ForeignKey to Pharmacy
- `inventory_item`: ForeignKey to InventoryItem
- `quantity`, `total_price`, `sale_time`: Sale details
- `extra_data`: JSON field
- `created_at`: Timestamp

### Order
- `pharmacy`: ForeignKey to Pharmacy
- `order_reference`, `status`, `items` (JSON), `total_amount`
- `created_at`, `updated_at`: Timestamps

### WebhookEvent
- `pharmacy`: ForeignKey to Pharmacy
- `event_type`, `payload` (JSON), `received_at`, `processed`

## API Overview

All API endpoints are under `/api/` and require an `X-API-KEY` header for authentication (per pharmacy).

| Resource         | Endpoint                  | Methods       |
|------------------|--------------------------|---------------|
| Pharmacies       | `/api/pharmacies/`       | CRUD          |
| Inventory Items  | `/api/inventory/`        | CRUD          |
| Sales            | `/api/sales/`            | CRUD          |
| Orders           | `/api/orders/`           | CRUD          |
| Webhook Events   | `/api/webhook-events/`   | CRUD          |

### Authentication
- Each request must include: `X-API-KEY: <pharmacy_api_key>`
- Only active pharmacies can access the API.

### API Documentation
- Swagger UI: [http://localhost:8000/swagger/](http://localhost:8000/swagger/)
- Redoc: [http://localhost:8000/redoc/](http://localhost:8000/redoc/)

## Setup & Installation

1. **Clone the repository**
   ```bash
   git clone <repo-url>
   cd Pharmacy-Connector-System
   ```
2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
3. **Configure the database**
   - By default, uses PostgreSQL. Update `DATABASE_URL` in environment or `settings.py` as needed.
4. **Apply migrations**
   ```bash
   python manage.py migrate
   ```
5. **Create a superuser (for admin access)**
   ```bash
   python manage.py createsuperuser
   ```
6. **Run the development server**
   ```bash
   python manage.py runserver
   ```
7. **Start Redis (for Channels and Celery)**
   - Ensure Redis is running on `localhost:6379`.
8. **Start Celery worker and beat (for background tasks)**
   ```bash
   celery -A pharmacy_connector worker -l info
   celery -A pharmacy_connector beat -l info
   ```

## Usage

- Access the admin dashboard at [http://localhost:8000/admin/](http://localhost:8000/admin/)
- Use the API endpoints with an `X-API-KEY` header (obtain API keys from the admin panel).
- Explore and test the API using Swagger or Redoc documentation.

## Webhooks
- Pharmacies can register a `webhook_url` to receive real-time notifications.
- Incoming webhook events are stored and can be processed asynchronously.

## Background Tasks
- Celery is configured for background processing (e.g., webhook handling, scheduled tasks).
- Django Channels enables real-time features (e.g., notifications, live updates).

## Customization
- Extend models or API endpoints as needed for your pharmacy workflow.
- Add new Celery tasks for background processing.

## License

This project is for demonstration and internal use. Please adapt and license as appropriate for your organization.
