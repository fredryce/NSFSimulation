#pragma once

#include <json.hpp>

#include <memory>
#include <unordered_map>

#include "simulation_common.hpp"

/*
    SimulationData class
    This class stores the recorded data for the simulation results
*/

class SimulationParticipant;
class SimulationNode;

using SimulationHop = std::pair<SimulationNode*, SimulationNode*>;

class SimulationData
{
public:
    explicit SimulationData();
    void RecordHop(SimulationParticipant* participant, SimulationHop hop);
    int GetHopCount(const std::string& name);
    float GetTime() { return _current_timestamp; }
    void ResetClock() { _current_timestamp = 0.f; }
    void AdvanceClock(float dt) { _delta_time = dt; _current_timestamp += dt; }
    float GetDeltaTime() const { return _delta_time; }
    float CurrentTime() const { return _current_timestamp; }
    int GetHops();
    float GetCoverage(int totalNodes);
private:
    std::unordered_map<std::string, std::vector<SimulationHop>> hop_data_;
    float _current_timestamp;
    float _delta_time;
};