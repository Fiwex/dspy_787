from dspy.teleprompt.mipro_optimizer import MIPRO

"""
===============================================================
DEPRECATED!!!
PLEASE USE MIPRO INSTEAD.
===============================================================

USAGE SUGGESTIONS:

The following code can be used to compile a optimized signature teleprompter using the BayesianSignatureOptimizer, and evaluate it on an end task:

from dspy.teleprompt import BayesianSignatureOptimizer

teleprompter = BayesianSignatureOptimizer(prompt_model=prompt_model, task_model=task_model, metric=metric, n=10, init_temperature=1.0)
kwargs = dict(num_threads=NUM_THREADS, display_progress=True, display_table=0)
compiled_prompt_opt = teleprompter.compile(program, devset=devset[:DEV_NUM], optuna_trials_num=100, max_bootstrapped_demos=3, max_labeled_demos=5, eval_kwargs=kwargs)
eval_score = evaluate(compiled_prompt_opt, devset=evalset[:EVAL_NUM], **kwargs)

Note that this teleprompter takes in the following parameters:

* prompt_model: The model used for prompt generation. When unspecified, defaults to the model set in settings (ie. dspy.settings.configure(lm=task_model)).
* task_model: The model used for prompt generation. When unspecified, defaults to the model set in settings (ie. dspy.settings.configure(lm=task_model)).
* metric: The task metric used for optimization.
* n: The number of new prompts and sets of fewshot examples to generate and evaluate. Default=10.
* init_temperature: The temperature used to generate new prompts. Higher roughly equals more creative. Default=1.0.
* verbose: Tells the method whether or not to print intermediate steps.
* track_stats: Tells the method whether or not to track statistics about the optimization process.
                If True, the method will track a dictionary with a key corresponding to the trial number, 
                and a value containing a dict with the following keys:
                    * program: the program being evaluated at a given trial
                    * score: the last average evaluated score for the program
                    * pruned: whether or not this program was pruned
                This information will be returned as attributes of the best program.
"""

class BayesianSignatureOptimizer(MIPRO):
    def __init__(self, prompt_model=None, task_model=None, teacher_settings={}, n=10, metric=None, init_temperature=1.0, verbose=False, track_stats=True, view_data_batch_size=10):
        print(u"\u001b[31m[WARNING] BayesianSignatureOptimizer has been deprecated and replaced with MIPRO.  BayesianSignatureOptimizer will be removed in a future release. \u001b[31m")
        
        super().__init__(prompt_model, task_model, teacher_settings,n,metric,init_temperature,verbose,track_stats,view_data_batch_size)