from neural_network.optimizers.sgd import sgd_update

def test_sgd():
    weights = [0.5, -0.2]
    grads = [0.1, -0.1]
    updated = sgd_update(weights, grads, lr=0.01)
    assert updated == [0.499, -0.199], f"Expected [0.499, -0.199], got {updated}"

if __name__ == "__main__":
    test_sgd()
    print("SGD test passed!")
