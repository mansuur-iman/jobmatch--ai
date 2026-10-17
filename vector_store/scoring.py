def distance_to_score(distance:float)->float:
    """convert cosine distance to a (0-100) score"""
    score = (1 - distance) * 100
    return round(max(0.0, min(100.0, score)), 2)