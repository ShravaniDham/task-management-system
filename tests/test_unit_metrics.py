"""UNIT TESTS - Agile metric calculations."""

from app import metrics


def test_velocity_is_completed_points():
    sprints = [{"completed": 10}, {"completed": 14}]
    assert metrics.calc_velocity(sprints) == [10, 14]


def test_average_of_values_and_empty_list():
    assert metrics.average([10, 20, 30]) == 20
    assert metrics.average([]) == 0


def test_defect_density():
    assert metrics.calc_defect_density(6, 1.5) == 4.0


def test_defect_density_with_zero_size_is_zero():
    assert metrics.calc_defect_density(3, 0) == 0


def test_lead_time_and_cycle_time():
    assert metrics.lead_time_days("2026-09-23", "2026-09-28") == 5
    assert metrics.cycle_time_days("2026-09-24", "2026-09-28") == 4


def test_sample_metrics_values():
    data = metrics.get_sample_metrics()
    assert data["average_velocity"] == 21.0
    assert data["overall_defect_density"] == 4.0
    assert data["average_lead_time"] == 9.0
    assert data["average_cycle_time"] == 4.0
    assert len(data["stories"]) == 5
