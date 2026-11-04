FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ ./app/

# Quick test run when container starts
CMD ["python", "-c", "from app.calculator import Calculator; print('Calculator Container Ready! 10 + 20 =', Calculator.add(10, 20))"]
