import numpy as np

def svdPCA(X, n_components=None):
    X_mean = np.mean(X, axis=0)
    X_centered = X - X_mean
    U, S, Vt = np.linalg.svd(X_centered, full_matrices=False)

    if n_components is None:
        n_components = min(X.shape)

    # Fix sign ambiguity
    components = Vt[:n_components]
    for i in range(components.shape[0]):
        max_abs_idx = np.argmax(np.abs(components[i]))
        if components[i, max_abs_idx] < 0:
            components[i] *= -1
            U[:, i] *= -1

    singular_values = S[:n_components]
    explained_variance = (S[:n_components] ** 2) / (X.shape[0] - 1)
    total_var = (S ** 2).sum() / (X.shape[0] - 1)
    explained_variance_ratio = explained_variance / total_var
    transformed_X = np.dot(X_centered, components.T)

    return transformed_X, components, explained_variance_ratio, singular_values
