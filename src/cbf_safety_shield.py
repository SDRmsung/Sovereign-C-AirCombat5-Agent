# -*- coding: utf-8 -*-
import numpy as np

class CBFSafetyShield:
    def __init__(self, safe_radius: float = 3000.0, gamma: float = 0.5):
        self.safe_radius = safe_radius
        self.gamma = gamma

    def compute_barrier(self, vip_pos: np.ndarray, enemy_pos: np.ndarray, enemy_vel: np.ndarray) -> bool:
        # Distance barrier: h(x) = dist - safe_radius >= 0
        rel_pos = enemy_pos - vip_pos
        dist = np.linalg.norm(rel_pos)
        h = dist - self.safe_radius
        # dh/dt = (rel_pos / dist) . (v_enemy - v_vip)
        # For threat moving towards VIP (closing velocity), dh/dt = dot(rel_pos/dist, enemy_vel)
        h_dot = np.dot(rel_pos / (dist + 1e-8), enemy_vel)
        # Safety invariance: h_dot + gamma * h >= 0
        return bool((h_dot + self.gamma * h) >= 0.0)

    def get_safe_heading(self, vip_pos: np.ndarray, threat_pos: np.ndarray) -> np.ndarray:
        evasion_dir = vip_pos - threat_pos
        norm = np.linalg.norm(evasion_dir)
        if norm < 1e-5:
            return np.array([1.0, 0.0, 0.0])
        return evasion_dir / norm
