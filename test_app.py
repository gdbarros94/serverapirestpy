import pytest
from flask import Flask, jsonify
from app import app
from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

@pytest.fixture
def auth_header(client):
    response = client.post('/login', json={
        'username': 'admin',
        'password': '123456'
    })
    assert response.status_code == 200
    access_token = response.json['access_token']
    return {'Authorization': f'Bearer {access_token}'}

def test_create_lead(client, auth_header):
    response = client.post('/leads', json={
        'name': 'Test Lead',
        'latitude': '10.000',
        'longitude': '20.000',
        'temperature': '30',
        'interest': 'High',
        'email': 'test@example.com',
        'telefone': '123456789'
    }, headers=auth_header)
    assert response.status_code == 201
    assert response.json['message'] == 'Lead criado com sucesso!'

def test_get_leads(client, auth_header):
    response = client.get('/leads', headers=auth_header)
    assert response.status_code == 200
    assert 'leads' in response.json

def test_update_lead(client, auth_header):
    response = client.post('/leads', json={
        'name': 'Update Lead',
        'latitude': '10.000',
        'longitude': '20.000',
        'temperature': '30',
        'interest': 'High',
        'email': 'update@example.com',
        'telefone': '123456789'
    }, headers=auth_header)
    assert response.status_code == 201

    lead_id = response.json['id']

    response = client.put(f'/leads/{lead_id}', json={
        'name': 'Updated Lead Name',
        'latitude': '10.000',
        'longitude': '20.000',
        'temperature': '35',
        'interest': 'Medium',
        'email': 'updated@example.com',
        'telefone': '987654321'
    }, headers=auth_header)
    assert response.status_code == 200
    assert response.json['message'] == 'Lead atualizado com sucesso!'

def test_delete_lead(client, auth_header):
    response = client.post('/leads', json={
        'name': 'Delete Lead',
        'latitude': '10.000',
        'longitude': '20.000',
        'temperature': '30',
        'interest': 'Low',
        'email': 'delete@example.com',
        'telefone': '123456789'
    }, headers=auth_header)
    assert response.status_code == 201

    lead_id = response.json['id']

    response = client.delete(f'/leads/{lead_id}', headers=auth_header)
    assert response.status_code == 200
    assert response.json['message'] == 'Lead deletado com sucesso!'

def test_login_invalid(client):
    response = client.post('/login', json={
        'username': 'admin',
        'password': 'wrongpassword'
    })
    assert response.status_code == 401
    assert response.json['error'] == 'Credenciais inválidas!'
