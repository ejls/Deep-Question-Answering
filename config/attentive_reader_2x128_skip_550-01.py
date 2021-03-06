from blocks.bricks import Tanh
from blocks.algorithms import BasicMomentum, AdaDelta, RMSProp, Adam, CompositeRule, StepClipping
from blocks.initialization import IsotropicGaussian, Constant

from model.attentive_reader import Model


batch_size = 32
sort_batch_count = 20

shuffle_questions = True

concat_ctx_and_question = False

n_entities = 550
embed_size = 200

ctx_lstm_size = [128, 128]
ctx_skip_connections = True

question_lstm_size = [128, 128]
question_skip_connections = True

attention_mlp_hidden = [100]
attention_mlp_activations = [Tanh()]

out_mlp_hidden = []
out_mlp_activations = []

step_rule = AdaDelta()

dropout = 0.1
w_noise = 0.05

valid_freq = 1000
save_freq = 1000
print_freq = 100

weights_init = IsotropicGaussian(0.01)
biases_init = Constant(0.)

