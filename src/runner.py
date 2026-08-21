# Copyright 2025 jxtngx
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Main entrypoint script for ML pipeline execution.

This module serves as the command-line interface for running machine
learning experiments. It parses arguments, loads configurations, and
delegates to appropriate modules for actual implementation.

Key responsibilities:
- Parse command-line arguments and configuration files
- Initialize the appropriate pipeline (train, evaluate, serve)
- Set up logging and experiment tracking
- Handle high-level error catching and reporting
- Provide a unified CLI interface for all ML operations

Usage:
    python src/runner.py train --config configs/experiment.yaml
    python src/runner.py evaluate --checkpoint path/to/model.pt
    python src/runner.py serve --model model.pt --port 8080

Integration points:
- Calls trainer.py for training execution
- Calls data.py for data pipeline setup
- Calls network.py for model creation
- Calls server.py for model serving
- Calls compute.py for resource management

Agent ownership:
- ml-engineer: CLI orchestration and pipeline coordination
"""
