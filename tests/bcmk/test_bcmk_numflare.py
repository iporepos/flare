"""
Short description of the module's purpose in 1–2 sentences.
todo improve major docstring

Features
--------
todo improve major docstring
- Feature 1 or key module
- Feature 2 or key module
- Feature 3 (optional)

Examples
--------
todo improve major docstring

"""
# --------------- imports ---------------
# import modules from other libs

# ---- native imports ----
import unittest

# ---- external imports ----
# fill [external imports]

# ---- project imports ----
from tests.conftest import RUN_BENCHMARKS, RUN_BENCHMARKS_XXL
from tests import conftest

# --------------- constants ---------------
# ---- public ----
# ---- private ----

# --------------- functions ---------------
# ---- public ----
def run_simulation(data_path, output_path):
    return None
# ---- private ----

# --------------- classes ---------------
# ---- public ----
# ---- private ----

@unittest.skipUnless(RUN_BENCHMARKS, "skipping benchmarks")
class BenchmarkModelTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """
        Prepare large datasets and output
        folders for benchmark testing.
        """
        # Example: download Catchment8 data if needed
        cls.data_path, cls.output_path = conftest.download_dataset(
            "Catchment8",
            url="https://example.com/Catchment8.zip"
        )

    def test_without_error(self):
        """
        Ensure the simulation runs
        without crashing.
        """
        conftest.testprint("simulation without error")
        try:
            results = run_simulation(
                data_path=self.data_path,
                output_path=self.output_path
            )
        except Exception as e:
            self.fail(f"Simulation crashed with error: {e}")

    @unittest.skipUnless(RUN_BENCHMARKS_XXL, "skipping long benchmarks")
    def test_full_model_run(self):
        """
        Benchmark test: run the full
        simulation and check outputs.
        """
        conftest.testprint("long simulation")
        # Run your simulation
        results = run_simulation(
            data_path=self.data_path,
            output_path=self.output_path
        )

        # Example assertions: basic validation of output
        self.assertIsNotNone(results)
        self.assertTrue((self.output_path / "summary.csv").exists())

    def test_model_performance(self):
        """
        Optional: measure execution
        time or performance.
        """
        conftest.testprint("model performance")
        import time
        start = time.time()
        # run
        run_simulation(
            data_path=self.data_path,
            output_path=self.output_path
        )

        elapsed = time.time() - start

        # Simple performance check (optional)
        conftest.testprint(f"model ran in {elapsed:.2f} seconds")
        # e.g., test fails if > 10 minutes
        self.assertLess(elapsed, 600)

# --------------- script ---------------
# standalone behaviour as a script
if __name__ == "__main__":
    from tests.conftest import RUN_BENCHMARKS
    RUN_BENCHMARKS = True
    unittest.main()