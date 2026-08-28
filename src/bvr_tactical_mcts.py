# -*- coding: utf-8 -*-
import numpy as np
from typing import Dict, List

class BVRTacticalMCTS:
    def __init__(self, num_simulations: int = 100):
        self.sims = num_simulations

    def dynamic_wta_assign(self, friendly_fighters: List[dict], enemy_targets: List[dict]) -> Dict[int, int]:
        # Weapon-Target Assignment via greedy heuristic (NP-Hard approximation)
        assignment = {}
        for f_idx, fighter in enumerate(friendly_fighters):
            f_pos = np.array(fighter["pos"])
            best_t_idx, min_threat_dist = -1, float("inf")
            for t_idx, target in enumerate(enemy_targets):
                t_pos = np.array(target["pos"])
                d = np.linalg.norm(f_pos - t_pos)
                if d < min_threat_dist:
                    min_threat_dist = d
                    best_t_idx = t_idx
            assignment[f_idx] = best_t_idx
        return assignment
