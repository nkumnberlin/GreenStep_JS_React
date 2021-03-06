import React from 'react'
import {Segment, Grid} from 'semantic-ui-react'
import {Progress} from 'react-sweet-progress';
import "react-sweet-progress/lib/style.css";

export const MyFootprintSegment = (prop) => {
    return (Object.values(prop).map((key) => {
                let per = Math.round(key.perc_amount);
                let color = key.color;
                return (
                    <Segment>
                        <Grid>
                            <Grid.Column width="16">
                            <p>{key.descr}</p>
                            </Grid.Column>
                            <Grid.Column width={key.width}>
                                
                                 <Progress
                                    percent={per}
                                    theme={{
                                        default: {
                                            color: color,
                                            symbol: key.emission
                                        },
                                        success: {
                                            color: color,
                                            symbol: key.emission
                                        },
                                        active: {
                                            color: color,
                                            symbol: key.emission
                                        }
                                    }}
                                />
                            </Grid.Column>
                        </Grid>
                    </Segment>
                )
            }
        )

    )

};