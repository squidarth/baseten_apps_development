# Functions that are linked to a worklet code block require a unique signature. In order to connect a worklet
# code block to a Python function the function has to use the arguments block_input, env, and context and
# return a JSON-serializable which becomes the input for the next block in the worklet.

# Learn more at https://docs.baseten.co/applications/worklets

# Here's an example of a simple passthrough using the required signature:

def passthrough(block_input, env, context):
    """
    Args:
      block_input (JSON-serializable): The input to this block.
      env (dict): A mutable dictionary that holds its state as
        it traverses the blocks of a worklet.
      context (Context): Provides helper methods for data access.
        See: https://docs.baseten.co/applications/worklets#context

    Returns:
      A JSON-serializable, which becomes the input to the next block in the worklet.
    """
    print(2)
    return block_input