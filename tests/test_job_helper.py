import os

import tempfile
from facefusion import state_manager
from facefusion.temp_helper import get_temp_directory_path
from facefusion.jobs.job_helper import get_step_output_path, get_step_temp_directory_path


def test_get_step_output_path() -> None:
        assert get_step_output_path('test-job', 0, 'test.mp4') == 'test-test-job-0.mp4'
        assert get_step_output_path('test-job', 0, 'test/test.mp4') == os.path.join('test', 'test-test-job-0.mp4')


def test_get_step_temp_directory_path() -> None:
        state_manager.init_item('temp_path', tempfile.gettempdir())
        step_output_path = get_step_output_path('test-job', 0, 'test.mp4')
        assert get_step_temp_directory_path('test-job', 0, 'test.mp4') == get_temp_directory_path(step_output_path)
