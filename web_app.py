#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Flask Web Application untuk Sistem Pakar Mitigasi Bencana Aceh
Implementasi Logika Matematika (Tabel Kebenaran)
"""

from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
from typing import Dict, Tuple
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for API requests

# ============================================
# PROPOSITIONAL LOGIC ENGINE
# ============================================

def AND(a: bool, b: bool) -> bool:
    """
    AND Gate (Conjunction)
    Returns True only if both inputs are True
    """
    return a and b


def OR(a: bool, b: bool) -> bool:
    """
    OR Gate (Disjunction)
    Returns True if at least one input is True
    """
    return a or b


def calculate_risk(p: bool, q: bool, r: bool) -> Tuple[bool, bool]:
    """
    Main Risk Calculation Function
    Formula: S = p ∧ (q ∨ r)
    
    Args:
        p: High Rainfall (Curah Hujan Tinggi)
        q: Deforestation/Palm Oil Land (Alih Fungsi Lahan Sawit)
        r: Bad Drainage (Sungai Dangkal/Sempit)
    
    Returns:
        Tuple of (q_or_r, result)
    """
    q_or_r = OR(q, r)
    result = AND(p, q_or_r)
    return q_or_r, result


# ============================================
# RECOMMENDATION ENGINE
# ============================================

def get_recommendation(p: bool, q: bool, r: bool, result: bool) -> Dict[str, str]:
    """
    Generate specific mitigation recommendations based on input combination
    """
    recommendations = {
        (False, False, False): {
            'icon': 'fa-sun',
            'color': 'text-green-600',
            'title': '✅ KONDISI IDEAL',
            'text': 'Tidak ada hujan, hutan masih terjaga, dan sungai dalam kondisi baik.\n'
                   'Rekomendasi: Lakukan pemantauan rutin dan jaga kelestarian lingkungan.'
        },
        (False, False, True): {
            'icon': 'fa-tools',
            'color': 'text-yellow-600',
            'title': '⚠️ PERBAIKAN DRAINASE',
            'text': 'Sungai dangkal/sempit memerlukan normalisasi.\n'
                   'Rekomendasi: Lakukan pengerukan sedimen dan pelebaran aliran sungai\n'
                   'untuk antisipasi hujan mendatang.'
        },
        (False, True, False): {
            'icon': 'fa-seedling',
            'color': 'text-yellow-600',
            'title': '⚠️ REBOISASI LAHAN',
            'text': 'Alih fungsi lahan sawit mengurangi daya serap air.\n'
                   'Rekomendasi: Implementasikan program reboisasi dan sistem agroforestri\n'
                   'untuk mencegah run-off tinggi.'
        },
        (False, True, True): {
            'icon': 'fa-exclamation',
            'color': 'text-orange-600',
            'title': '⚠️ SIAGA ANTISIPASI',
            'text': 'Kombinasi lahan rusak dan drainase buruk sangat berisiko.\n'
                   'Rekomendasi: Meskipun belum hujan, segera lakukan perbaikan infrastruktur\n'
                   'dan siapkan jalur evakuasi.'
        },
        (True, False, False): {
            'icon': 'fa-umbrella',
            'color': 'text-blue-600',
            'title': '✅ HUJAN AMAN TERKENDALI',
            'text': 'Hujan deras, namun hutan lebat menyerap air dengan baik dan sungai lancar.\n'
                   'Rekomendasi: Kondisi aman, tetap pantau intensitas hujan dan\n'
                   'ketinggian air sungai.'
        },
        (True, False, True): {
            'icon': 'fa-water',
            'color': 'text-red-600',
            'title': '🚨 PERINGATAN BANJIR - DRAINASE BURUK',
            'text': 'Hujan deras dengan sungai dangkal/sempit menyebabkan luapan air.\n'
                   'TINDAKAN SEGERA:\n'
                   '- Evakuasi warga di bantaran sungai\n'
                   '- Tutup akses jalan rendah\n'
                   '- Aktifkan posko bencana'
        },
        (True, True, False): {
            'icon': 'fa-mountain',
            'color': 'text-red-600',
            'title': '🚨 PERINGATAN BANJIR - RUN-OFF TINGGI',
            'text': 'Hujan deras pada lahan sawit memicu run-off ekstrem.\n'
                   'TINDAKAN SEGERA:\n'
                   '- Evakuasi warga di lereng bukit dan daerah aliran sungai\n'
                   '- Waspadai banjir bandang dan tanah longsor'
        },
        (True, True, True): {
            'icon': 'fa-exclamation-triangle',
            'color': 'text-red-700',
            'title': '🔴 BAHAYA MAKSIMAL - EVAKUASI DARURAT',
            'text': 'KONDISI KRITIS! Kombinasi hujan deras, lahan rusak, dan drainase buruk.\n'
                   'TINDAKAN DARURAT:\n'
                   '- Evakuasi massal ke tempat tinggi\n'
                   '- Aktifkan semua posko\n'
                   '- Koordinasi dengan BNPB\n'
                   '- Siapkan bantuan logistik'
        }
    }
    
    return recommendations.get((p, q, r), {
        'icon': 'fa-question',
        'color': 'text-gray-600',
        'title': 'Unknown',
        'text': 'No recommendation available'
    })


def generate_truth_table() -> list:
    """
    Generate complete truth table with all 8 combinations
    """
    table = []
    for i in range(8):
        p = bool(i & 4)
        q = bool(i & 2)
        r = bool(i & 1)
        
        q_or_r, result = calculate_risk(p, q, r)
        
        table.append({
            'p': p,
            'q': q,
            'r': r,
            'q_or_r': q_or_r,
            'result': result
        })
    
    return table


# ============================================
# ARTICLES DATA
# ============================================

def get_articles() -> list:
    """
    Get list of disaster mitigation articles with photos
    """
    articles = [
        {
            'id': 1,
            'category': 'Tips',
            'title': 'Tips Mitigasi Banjir untuk Masyarakat Aceh',
            'excerpt': 'Panduan lengkap untuk masyarakat dalam menghadapi ancaman banjir. Termasuk persiapan darurat, jalur evakuasi, dan perlengkapan yang harus disiapkan.',
            'date': '2025-01-15',
            'image': 'https://images.unsplash.com/photo-1741081288260-877057e3fa27?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NTAwNDR8MHwxfHNlYXJjaHwyfHxDb21tdW5pdHklMjB2b2x1bnRlZXJzJTIwaGVscGluZyUyMGR1cmluZyUyMGZsb29kJTIwZGlzYXN0ZXIlMkMlMjBwZW9wbGUlMjBldmFjdWF0aW5nJTJDJTIwZW1lcmdlbmN5JTIwcmVzcG9uc2UlMjB0ZWFtJTIwcGVvcGxlfGVufDB8MHx8fDE3NjQ3MzIwNDZ8MA&ixlib=rb-4.1.0&q=85',
            'image_alt': 'Tim relawan membantu evakuasi saat banjir - Photo by Iqro Rinaldi on Unsplash',
            'author': 'BNPB Aceh'
        },
        {
            'id': 2,
            'category': 'Teknologi',
            'title': 'Sistem Peringatan Dini Bencana di Aceh',
            'excerpt': 'Teknologi terkini dalam sistem peringatan dini banjir menggunakan sensor cuaca, monitoring sungai, dan alert system berbasis SMS untuk masyarakat.',
            'date': '2025-01-10',
            'image': 'https://images.pexels.com/photos/29436201/pexels-photo-29436201.jpeg',
            'image_alt': 'Stasiun cuaca untuk monitoring bencana - Photo by Charles Criscuolo on Pexels',
            'author': 'BMKG Aceh'
        },
        {
            'id': 3,
            'category': 'Lingkungan',
            'title': 'Program Reboisasi Hutan untuk Cegah Banjir',
            'excerpt': 'Pentingnya reboisasi hutan dan konservasi lahan untuk mengurangi risiko banjir. Program penanaman 10,000 pohon di daerah rawan banjir Aceh.',
            'date': '2025-01-05',
            'image': 'https://images.unsplash.com/photo-1632397782627-29040fc97a4b?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NTAwNDR8MHwxfHNlYXJjaHw5fHxGb3Jlc3QlMjByZWZvcmVzdGF0aW9uJTJDJTIwcGxhbnRpbmclMjB0cmVlcyUyQyUyMGdyZWVuJTIwbGFuZHNjYXBlJTJDJTIwZW52aXJvbm1lbnRhbCUyMGNvbnNlcnZhdGlvbnxlbnwwfDB8fGdyZWVufDE3NjQ3MzIwNDZ8MA&ixlib=rb-4.1.0&q=85',
            'image_alt': 'Hutan hijau yang lebat - Photo by boris misevic on Unsplash',
            'author': 'Dinas Lingkungan Hidup'
        },
        {
            'id': 4,
            'category': 'Infrastruktur',
            'title': 'Normalisasi Sungai dan Perbaikan Drainase',
            'excerpt': 'Proyek normalisasi sungai dan perbaikan sistem drainase di 15 titik rawan banjir. Target pengerukan 50,000 m³ sedimen untuk kelancaran aliran air.',
            'date': '2024-12-28',
            'image': 'https://images.unsplash.com/photo-1562544294-3484049612ce?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NTAwNDR8MHwxfHNlYXJjaHwxfHxSaXZlciUyMGRyYWluYWdlJTIwc3lzdGVtJTJDJTIwd2F0ZXIlMjBtYW5hZ2VtZW50JTIwaW5mcmFzdHJ1Y3R1cmUlMkMlMjBmbG9vZCUyMGNvbnRyb2x8ZW58MHwwfHxibHVlfDE3NjQ3MzIwNDZ8MA&ixlib=rb-4.1.0&q=85',
            'image_alt': 'Sistem drainase dan pengelolaan air - Photo by Chandler Cruttenden on Unsplash',
            'author': 'Dinas Pekerjaan Umum'
        },
        {
            'id': 5,
            'category': 'Kesiapsiagaan',
            'title': 'Kesiapsiagaan Menghadapi Musim Hujan 2025',
            'excerpt': 'Persiapan menghadapi musim hujan dengan prediksi curah hujan tinggi. Checklist lengkap untuk keluarga dan komunitas dalam mengantisipasi banjir.',
            'date': '2024-12-20',
            'image': 'https://images.unsplash.com/photo-1705102659473-97da402ca422?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NTAwNDR8MHwxfHNlYXJjaHwyM3x8SGVhdnklMjByYWluZmFsbCUyQyUyMHN0b3JtJTIwY2xvdWRzJTJDJTIwcmFpbnklMjB3ZWF0aGVyJTJDJTIwZmxvb2RpbmclMjB3YXRlcnxlbnwwfDB8fGJsdWV8MTc2NDczMjA0N3ww&ixlib=rb-4.1.0&q=85',
            'image_alt': 'Awan badai menandakan hujan deras - Photo by Raychel Sanner on Unsplash',
            'author': 'BPBD Aceh'
        },
        {
            'id': 6,
            'category': 'Edukasi',
            'title': 'Pelatihan Tanggap Darurat untuk Relawan',
            'excerpt': 'Program pelatihan tanggap darurat bencana untuk relawan komunitas. Materi meliputi pertolongan pertama, evakuasi, dan koordinasi tim respons cepat.',
            'date': '2024-12-15',
            'image': 'https://images.unsplash.com/photo-1581094373271-1fa59e2ab263?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NTAwNDR8MHwxfHNlYXJjaHwxfHxFbWVyZ2VuY3klMjBwcmVwYXJlZG5lc3MlMjB0cmFpbmluZyUyQyUyMGRpc2FzdGVyJTIwcmVzcG9uc2UlMjB0ZWFtJTJDJTIwY29tbXVuaXR5JTIwbWVldGluZyUyMHBlb3BsZXxlbnwwfDB8fHwxNzY0NzMyMDQ2fDA&ixlib=rb-4.1.0&q=85',
            'image_alt': 'Pelatihan tim tanggap darurat - Photo by ThisisEngineering on Unsplash',
            'author': 'PMI Aceh'
        }
    ]
    
    return articles


# ============================================
# FLASK ROUTES
# ============================================

@app.route('/')
def index():
    """Serve the main web interface"""
    return render_template('index.html')


@app.route('/enhanced')
def index_enhanced():
    """Serve the enhanced web interface with advanced features"""
    return render_template('index_enhanced.html')


@app.route('/api/calculate', methods=['POST'])
def api_calculate():
    """
    API endpoint to calculate flood risk
    
    Expected JSON body:
    {
        "p": true/false,
        "q": true/false,
        "r": true/false
    }
    
    Returns:
    {
        "p": bool,
        "q": bool,
        "r": bool,
        "q_or_r": bool,
        "result": bool,
        "recommendation": {...}
    }
    """
    try:
        data = request.get_json()
        
        p = bool(data.get('p', False))
        q = bool(data.get('q', False))
        r = bool(data.get('r', False))
        
        q_or_r, result = calculate_risk(p, q, r)
        recommendation = get_recommendation(p, q, r, result)
        
        return jsonify({
            'success': True,
            'p': p,
            'q': q,
            'r': r,
            'q_or_r': q_or_r,
            'result': result,
            'recommendation': recommendation
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400


@app.route('/api/truth-table', methods=['GET'])
def api_truth_table():
    """
    API endpoint to get complete truth table
    
    Returns:
    {
        "table": [...]
    }
    """
    try:
        table = generate_truth_table()
        return jsonify({
            'success': True,
            'table': table
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400


@app.route('/api/articles', methods=['GET'])
def api_articles():
    """
    API endpoint to get all articles
    
    Returns:
    {
        "articles": [...]
    }
    """
    try:
        articles = get_articles()
        return jsonify({
            'success': True,
            'articles': articles
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400


@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'service': 'Sistem Pakar Mitigasi Bencana Aceh',
        'version': '1.0.0'
    })


# ============================================
# ERROR HANDLERS
# ============================================

@app.errorhandler(404)
def not_found(error):
    return jsonify({
        'success': False,
        'error': 'Endpoint not found'
    }), 404


@app.errorhandler(500)
def internal_error(error):
    return jsonify({
        'success': False,
        'error': 'Internal server error'
    }), 500


# ============================================
# MAIN ENTRY POINT
# ============================================

if __name__ == '__main__':
    # Create templates directory if it doesn't exist
    os.makedirs('templates', exist_ok=True)
    
    # Run Flask development server
    print("=" * 70)
    print("🌊 SISTEM PAKAR MITIGASI BENCANA ACEH - WEB VERSION 🌊".center(70))
    print("=" * 70)
    print()
    print("🚀 Starting Flask server...")
    print("📍 Server akan berjalan di: http://localhost:5000")
    print("📍 API Documentation:")
    print("   - POST /api/calculate - Calculate flood risk")
    print("   - GET  /api/truth-table - Get complete truth table")
    print("   - GET  /api/articles - Get disaster mitigation articles")
    print("   - GET  /api/health - Health check")
    print()
    print("Press CTRL+C to stop the server")
    print("=" * 70)
    print()
    
    app.run(debug=True, host='0.0.0.0', port=5000)