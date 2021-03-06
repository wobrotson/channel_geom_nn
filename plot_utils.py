import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def compare_plot(df, y_train, y_test, pred_train, pred_test):
    """
    Plot comparison of the predictions and actual values (1:1 plots).
    """
    fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(9,4))

    ax[0].plot(y_train[:,1], pred_train[:,1], 'o', alpha=0.2)
    ax[0].plot(y_test[:,1], pred_test[:,1], 'o', alpha=0.8)
    ax[0].plot([df['Hbf.m'].min()/10, df['Hbf.m'].max()*10], [df['Hbf.m'].min()/10, df['Hbf.m'].max()*10], 'k-', lw=2)
    ax[0].axis('square')
    ax[0].set_title('depth H, (m)')
    ax[0].set_yscale('log')
    ax[0].set_xscale('log')
    ax[0].set_xlabel('actual')
    ax[0].set_ylabel('pred')
    ax[0].set_xlim([df['Hbf.m'].min()/10, df['Hbf.m'].max()*10])
    ax[0].set_ylim([df['Hbf.m'].min()/10, df['Hbf.m'].max()*10])
    ax[0].legend(['train', 'test'], loc = 'upper left')

    ax[1].plot(y_train[:,0], pred_train[:,0], 'o', alpha=0.2)
    ax[1].plot(y_test[:,0], pred_test[:,0], 'o', alpha=0.8)
    ax[1].plot([df['Bbf.m'].min()/10, df['Bbf.m'].max()*10], [df['Bbf.m'].min()/10, df['Bbf.m'].max()*10], 'k-', lw=2)
    ax[1].axis('square')
    ax[1].set_title('width B, (m)')
    ax[1].set_yscale('log')
    ax[1].set_xscale('log')
    ax[1].set_xlabel('actual')
    ax[1].set_xlim([df['Bbf.m'].min()/10, df['Bbf.m'].max()*10])
    ax[1].set_ylim([df['Bbf.m'].min()/10, df['Bbf.m'].max()*10])

    ax[2].plot(y_train[:,2], pred_train[:,2], 'o', alpha=0.2)
    ax[2].plot(y_test[:,2], pred_test[:,2], 'o', alpha=0.8)
    ax[2].plot([df['S'].min()/10, df['S'].max()*10], [df['S'].min()/10, df['S'].max()*10], 'k-', lw=2)
    ax[2].axis('square')
    ax[2].set_title('slope S, (1)')
    ax[2].set_yscale('log')
    ax[2].set_xscale('log')
    ax[2].set_xlabel('actual')
    ax[2].set_xlim([df['S'].min()/10, df['S'].max()*10])
    ax[2].set_ylim([df['S'].min()/10, df['S'].max()*10])

    plt.tight_layout()
    return fig
