from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from src.models.user import db
from src.models.task import Task
from datetime import datetime

task_bp = Blueprint('task', __name__)

@task_bp.route('/tasks', methods=['GET'])
@jwt_required()
def get_tasks():
    try:
        current_user_id = int(get_jwt_identity())
        
        # Get query parameters for filtering and sorting
        completed = request.args.get('completed')
        priority = request.args.get('priority')
        sort_by = request.args.get('sort_by', 'created_at')
        sort_order = request.args.get('sort_order', 'desc')
        
        # Build query
        query = Task.query.filter_by(user_id=current_user_id)
        
        # Apply filters
        if completed is not None:
            completed_bool = completed.lower() == 'true'
            query = query.filter_by(completed=completed_bool)
        
        if priority:
            query = query.filter_by(priority=priority)
        
        # Apply sorting
        if sort_by in ['created_at', 'updated_at', 'due_date', 'title', 'priority']:
            if sort_order.lower() == 'asc':
                query = query.order_by(getattr(Task, sort_by).asc())
            else:
                query = query.order_by(getattr(Task, sort_by).desc())
        
        tasks = query.all()
        return jsonify([task.to_dict() for task in tasks]), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@task_bp.route('/tasks', methods=['POST'])
@jwt_required()
def create_task():
    try:
        current_user_id = int(get_jwt_identity())
        data = request.json
        
        # Validate required fields
        if not data or not data.get('title'):
            return jsonify({'error': 'Title is required'}), 400
        
        # Parse due_date if provided
        due_date = None
        if data.get('due_date'):
            try:
                due_date = datetime.fromisoformat(data['due_date'].replace('Z', '+00:00'))
            except ValueError:
                return jsonify({'error': 'Invalid due_date format. Use ISO format.'}), 400
        
        # Create new task
        task = Task(
            title=data['title'],
            description=data.get('description', ''),
            priority=data.get('priority', 'medium'),
            due_date=due_date,
            user_id=current_user_id
        )
        
        db.session.add(task)
        db.session.commit()
        
        return jsonify({
            'message': 'Task created successfully',
            'task': task.to_dict()
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@task_bp.route('/tasks/<int:task_id>', methods=['GET'])
@jwt_required()
def get_task(task_id):
    try:
        current_user_id = int(get_jwt_identity())
        task = Task.query.filter_by(id=task_id, user_id=current_user_id).first()
        
        if not task:
            return jsonify({'error': 'Task not found'}), 404
        
        return jsonify({'task': task.to_dict()}), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@task_bp.route('/tasks/<int:task_id>', methods=['PUT'])
@jwt_required()
def update_task(task_id):
    try:
        current_user_id = int(get_jwt_identity())
        task = Task.query.filter_by(id=task_id, user_id=current_user_id).first()
        
        if not task:
            return jsonify({'error': 'Task not found'}), 404
        
        data = request.json
        
        # Update fields if provided
        if 'title' in data:
            task.title = data['title']
        if 'description' in data:
            task.description = data['description']
        if 'completed' in data:
            task.completed = data['completed']
        if 'priority' in data:
            task.priority = data['priority']
        if 'due_date' in data:
            if data['due_date']:
                try:
                    task.due_date = datetime.fromisoformat(data['due_date'].replace('Z', '+00:00'))
                except ValueError:
                    return jsonify({'error': 'Invalid due_date format. Use ISO format.'}), 400
            else:
                task.due_date = None
        
        task.updated_at = datetime.utcnow()
        db.session.commit()
        
        return jsonify({
            'message': 'Task updated successfully',
            'task': task.to_dict()
        }), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@task_bp.route('/tasks/<int:task_id>', methods=['DELETE'])
@jwt_required()
def delete_task(task_id):
    try:
        current_user_id = int(get_jwt_identity())
        task = Task.query.filter_by(id=task_id, user_id=current_user_id).first()
        
        if not task:
            return jsonify({'error': 'Task not found'}), 404
        
        db.session.delete(task)
        db.session.commit()
        
        return jsonify({'message': 'Task deleted successfully'}), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@task_bp.route('/tasks/stats', methods=['GET'])
@jwt_required()
def get_task_stats():
    try:
        current_user_id = int(get_jwt_identity())
        
        total_tasks = Task.query.filter_by(user_id=current_user_id).count()
        completed_tasks = Task.query.filter_by(user_id=current_user_id, completed=True).count()
        pending_tasks = total_tasks - completed_tasks
        
        # Tasks by priority
        high_priority = Task.query.filter_by(user_id=current_user_id, priority='high', completed=False).count()
        medium_priority = Task.query.filter_by(user_id=current_user_id, priority='medium', completed=False).count()
        low_priority = Task.query.filter_by(user_id=current_user_id, priority='low', completed=False).count()
        
        return jsonify({
            'total_tasks': total_tasks,
            'completed_tasks': completed_tasks,
            'pending_tasks': pending_tasks,
            'priority_breakdown': {
                'high': high_priority,
                'medium': medium_priority,
                'low': low_priority
            }
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

